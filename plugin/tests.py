from jsdoc_sort import JsdocSorter

import unittest
import vimmock
vimmock.patch_vim()
import vim

vim.setup_text("import React from 'react';" +
"import PropTypes from 'prop-types';\n" +
"import { AsyncPaginateBase } from 'react-select-async-paginate';\n" +
"import NumberTextBox from '../../shared/components/UI/numberTextBox/NumberTextBox';\n" +
"import SoldReportFiltersTagCloudTag from './SoldReportFiltersTagCloudTag/SoldReportFiltersTagCloudTag';\n" +
"\n" +
"\n" +
"const soldReportFilters = /** @param {SoldReportFiltersProps} props */ props => {\n" +
"  const dateRanges = props.filterDateRange.map(filter => <option key={filter.value} value={filter.value}>{filter.displayValue}</option>);\n" +
"  const sources = props.filterSource.map(source => <option key={source.value} value={source.value}>{source.displayValue}</option>);\n" +
"  let marketAreas;\n" +
"  if (props.filterMarketArea) {\n" +
"    marketAreas = props.filterMarketArea.map(ma => <option key={ma.stateOrProvince} value={ma.stateOrProvince}>{ma.country} - {ma.stateOrProvinceName}</option>);\n" +
"  }\n" +
"\n" +
"  let appliedFilters = null;\n" +
"  if (tags.length > 0) {\n" +
"    appliedFilters = (\n" +
"      <React.Fragment>\n" +
"        <label htmlFor="" className=\"applied-filters\">Applied filters</label>\n" +
"        <div className=\"tag-cloud\">\n" +
"          {tags}\n" +
"        </div>\n" +
"      </React.Fragment>\n" +
"    );\n" +
"  }\n" +
"\n" +
"  if (!props.show) {\n" +
"    return null;\n" +
"  }\n" +
"\n" +
"  return (\n" +
"      <div className=\"advanced-filters\">\n" +
"        <h6>Advanced: Choose Filter &amp; Set Range</h6>\n" +
"        <div className=\"flex-wrapper\">\n" +
"            <label htmlFor="">Filter</label>\n" +
"            <select\n" +
"                className=\"choose-advanced-filter\"\n" +
"                disabled={props.loadingFilters || sizeMeters.length < 1}\n" +
"                id=\"choose-advanced-filter\"\n" +
"                name=\"choose-advanced-filter\"\n" +
"                onChange={e => props.onSizeMeterChange(props.filterSizeMeters.find(sm => sm.code === e.target.value))}\n" +
"                value={props.filterSelectedSizeMeterCode}\n" +
"            >\n" +
"                <option key="" value=""></option>\n" +
"                {sizeMeters}\n" +
"            </select>\n" +
"        </div>\n" +
"      </div>\n" +
"  )\n" +
"}\n" +
"\n" +
"soldReportFilters.propTypes = {\n" +
"  clearOptionsCache: PropTypes.number.isRequired,\n" +
"  filterDateRange: PropTypes.array.isRequired,\n" +
"  filterMarketArea: PropTypes.array.isRequired,\n" +
"  filterSelectedDateRange: PropTypes.string.isRequired,\n" +
"  filterSelectedMarketArea: PropTypes.string.isRequired,\n" +
"  filterSelectedOptions: PropTypes.array.isRequired,\n" +
"  filterSelectedSizeMeterCode: PropTypes.string.isRequired,\n" +
"  filterSelectedSizeMeterFrom: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,\n" +
"  filterSelectedSizeMeterFromValidation: PropTypes.any.isRequired,\n" +
"  filterSelectedSizeMeterRanges: PropTypes.array.isRequired,\n" +
"  filterSelectedSizeMeterTo: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,\n" +
"  filterSelectedSizeMeterToValidation: PropTypes.any.isRequired,\n" +
"  filterSelectedSource: PropTypes.string.isRequired,\n" +
"  filterSizeMeters: PropTypes.array.isRequired,\n" +
"  filterSource: PropTypes.array.isRequired,\n" +
"  loadingFilters: PropTypes.bool.isRequired,\n" +
"  onDateRangeChanged: PropTypes.func.isRequired,\n" +
"  onFilterSelectedSizeMeterFromChanged: PropTypes.func.isRequired,\n" +
"  onFilterSelectedSizeMeterToChanged: PropTypes.func.isRequired,\n" +
"  onHide: PropTypes.func.isRequired,\n" +
"  onLoadOptions: PropTypes.func.isRequired,\n" +
"  onMarketAreaChanged: PropTypes.func.isRequired,\n" +
"  onOptionRemove: PropTypes.func.isRequired,\n" +
"  onOptionSuggestLeave: PropTypes.func.isRequired,\n" +
"  onOptionSuggestionInput: PropTypes.func.isRequired,\n" +
"  onOptionSuggestionSelected: PropTypes.func.isRequired,\n" +
"  onSizeMeterChange: PropTypes.func.isRequired,\n" +
"  onSizeMeterFilterAdded: PropTypes.func.isRequired,\n" +
"  onSizeMeterRangeRemove: PropTypes.func.isRequired,\n" +
"  onSourceChanged: PropTypes.func.isRequired,\n" +
"  optionSuggestions: PropTypes.array.isRequired,\n" +
"  show: PropTypes.bool.isRequired\n" +
"}\n" +
"\n" +
"/**\n" +
" * @typedef SoldReportFiltersProps\n" +
" * @property {Array<{displayValue: string, value: number}>} filterDateRange\n" +
" * @property {import('IronTypes').OtherEquipmentStateOrProvince[]} filterMarketArea\n" +
" * @property {string} filterSelectedDateRange\n" +
" * @property {string} filterSelectedSizeMeterCode\n" +
" * @property {string} filterSelectedSource\n" +
" * @property {(event: any) => void} onDateRangeChanged\n" +
" * @property {string | number} filterSelectedSizeMeterFrom\n" +
" * @property {{message: string, min: number, max: number, valid: boolean}} filterSelectedSizeMeterFromValidation\n" +
" * @property {Array<import('IronTypes').SizeMeterRangeNamed>} filterSelectedSizeMeterRanges\n" +
" * @property {string | number} filterSelectedSizeMeterTo\n" +
" * @property {{message: string, min: number, max: number, valid: boolean}} filterSelectedSizeMeterToValidation\n" +
" * @property {any[]} filterSelectedOptions\n" +
" * @property {Array<{code: string, description: string, recordType: string, min: number, max: number}>} filterSizeMeters\n" +
" * @property {Array<{displayValue: string, value: string}>} filterSource\n" +
" * @property {boolean} loadingFilters\n" +
" * @property {(range) => void} onSizeMeterRangeRemove\n" +
" * @property {(opt) => void} onOptionRemove\n" +
" * @property {boolean} show\n" +
" * @property {number} clearOptionsCache\n" +
" * @property {(e: any) => void} onSourceChanged\n" +
" * @property {(e: any) => void} onSizeMeterFilterAdded\n" +
" * @property {(e: any) => onFilterSelectedSizeMeterToChanged} onFilterSelectedSizeMeterToChanged\n" +
" */\n" +
"\n" +
"export default soldReportFilters;")
JsdocSorter(vim).sort()
for line in vim.current.buffer:
    print(line)
print('done')
