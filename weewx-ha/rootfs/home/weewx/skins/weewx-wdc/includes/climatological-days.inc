<!--prettier-ignore-->
#errorCatcher Echo
#encoding UTF-8
#set $show_climatogram_year = $context == 'year' and $DisplayOptions.get("climatogram_enable_year_stats", False)
#set $show_climatogram_alltime = $context == 'alltime' and $DisplayOptions.get("climatogram_enable_stats", False)

<script
  type="module"
  src="https://1.www.s81c.com/common/carbon/web-components/version/v1.21.0/structured-list.min.js"
></script>

<script
  type="module"
  src="https://1.www.s81c.com/common/carbon/web-components/version/v1.21.0/tooltip.min.js"
></script>

<script
  type="module"
  src="https://1.www.s81c.com/common/carbon/web-components/version/v1.21.0/tabs.min.js"
></script>
<!--prettier-ignore-->
<bx-tabs trigger-content="Select an item" value="table" type="container">
  <bx-tab id="tab-table" target="panel-table" value="table">Table</bx-tab>
  #if $getattr($get_time_span_from_context($context, $day, $week, $month, $year, $alltime, $yesterday), 'rain').has_data
  <bx-tab
    id="tab-diagram-rain"
    target="panel-diagram-rain"
    value="diagram-rain"
  >
    $gettext('rainDays')
  </bx-tab>
  #end if
  #if $getattr($get_time_span_from_context($context, $day, $week, $month, $year, $alltime, $yesterday), 'outTemp').has_data
  <bx-tab
    id="tab-diagram-temp-avg"
    target="panel-diagram-temp-avg"
    value="diagram-temp-avg"
  >
    $gettext('Avg.') $obs.label.outTemp
  </bx-tab>
  #end if
  #if $show_climatogram_year or $show_climatogram_alltime
  <bx-tab id="tab-climatogram" target="panel-climatogram" value="climatogram"
    >$gettext('Climatogram')</bx-tab
  >
  #end if
</bx-tabs>

<div class="bx-ce-demo-devenv--tab-panels">
  <div
    class="climatological-tile"
    id="panel-table"
    role="tabpanel"
    aria-labelledby="tab-table"
    hidden
  >
    <bx-structured-list>
      <bx-structured-list-head>
        <bx-structured-list-header-row>
          <bx-structured-list-header-cell
            >$gettext("Climatological day")</bx-structured-list-header-cell
          >
          <bx-structured-list-header-cell
            >$gettext("Number of days")</bx-structured-list-header-cell
          >
          <bx-structured-list-header-cell>
            <span class="hide-mobile">$gettext("Description")</span>
          </bx-structured-list-header-cell>
        </bx-structured-list-header-row>
      </bx-structured-list-head>
      <bx-structured-list-body>
        #for $clim_day in $DisplayOptions.get('climatological_days')
        <bx-structured-list-row data-test="$clim_day">
          <bx-structured-list-cell>$gettext($clim_day)</bx-structured-list-cell>
          <bx-structured-list-cell>
            <!--prettier-ignore-->
            #set $time_span = $get_time_span_from_context($context, $day, $week, $month, $year, $alltime, $yesterday)
            $get_climatological_day($clim_day, $time_span.start.raw, $time_span.end.raw)
          </bx-structured-list-cell>
          <bx-structured-list-cell>
            <div data-floating-menu-container style="position: relative">
              <bx-tooltip>
                <bx-tooltip-body>
                  <p>
                    <!--prettier-ignore-->
                    $get_climatological_day_description($clim_day)
                  </p>
                </bx-tooltip-body>
              </bx-tooltip>
            </div>
            <span>
              <!--prettier-ignore-->
              $get_climatological_day_description($clim_day)
            </span>
          </bx-structured-list-cell>
        </bx-structured-list-row>
        #end for
      </bx-structured-list-body>
    </bx-structured-list>
  </div>
  <!--prettier-ignore-->
  #if $getattr($get_time_span_from_context($context, $day, $week, $month, $year, $alltime, $yesterday), 'rain').has_data
  <div
    id="panel-diagram-rain"
    role="tabpanel"
    aria-labelledby="tab-diagram-rain"
    hidden
  >
    <script>
      /* prettier-ignore */
      #set $obs_context = $get_time_span_from_context($context, $day, $week, $month, $year, $alltime, $yesterday)
      var calendarDataRain = $get_calendar_data('rain', 'sum', $obs_context.start.raw, $obs_context.end.raw);
    </script>
    <div
      class="calendar-diagram-clim-wrap"
      data-value="calendarDataRain"
      data-obs="rain"
      data-unit="$unit.label.rain"
      data-color="$get_calendar_color('rain')"
      data-heading="$gettext('rainDays')"
    ></div>
  </div>
  #end if
  <!--prettier-ignore-->
  #if $getattr($get_time_span_from_context($context, $day, $week, $month, $year, $alltime, $yesterday), 'outTemp').has_data
  <div
    id="panel-diagram-temp-avg"
    role="tabpanel"
    aria-labelledby="tab-diagram-temp-avg"
    hidden
  >
    <script>
      /* prettier-ignore */
      #set $obs_context = $get_time_span_from_context($context, $day, $week, $month, $year, $alltime, $yesterday)
      var calendarDataTempAvg = $get_calendar_data('outTemp', 'avg', $obs_context.start.raw, $obs_context.end.raw);
    </script>
    <div
      class="calendar-diagram-clim-wrap"
      data-value="calendarDataTempAvg"
      data-obs="outTemp"
      data-unit="$unit.label.outTemp"
      data-color="$get_calendar_color('outTemp')"
      data-heading="${obs.label.outTemp} $gettext('Avg.')"
    ></div>
  </div>
  #end if
  <!-- prettier-ignore -->
  #if $show_climatogram_year or $show_climatogram_alltime
  <!-- prettier-ignore -->
  <div
    id="panel-climatogram"
    role="tabpanel"
    aria-labelledby="tab-climatogram"
    hidden
  >
    #if $show_climatogram_year
      <div class="year">
        #set global $comb_obs = "climatogram_year"
        #set global $combined_diagram = $DisplayOptions.get("diagrams", {}).get("combined_observations", {}).get('climatogram_year', {})
        #set global $diagram_index = 9999
        #include "includes/combined-diagram-tile.inc"
      </div>
    #else if $show_climatogram_alltime
      <div class="alltime">
        #set global $comb_obs = "climatogram_statistics"
        #set global $combined_diagram = $DisplayOptions.get("diagrams", {}).get("combined_observations", {}).get('climatogram_statistics', {})
        #set global $diagram_index = 9999
        #include "includes/combined-diagram-tile.inc"
      </div>
    #end if
  </div>
  #end if
</div>
