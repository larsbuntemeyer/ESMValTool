library(lintr)

args <- commandArgs(trailingOnly = TRUE)
check_paths <- list("esmvaltool", "tests")

root_folder <- args[1]
has_errors <- FALSE
linters <- with_defaults(line_length_linter(79))

for (path in check_paths) { # nolint
  check_path <- file.path(root_folder, path)
  for (file in list.files(
    check_path,
    recursive = TRUE,
    include.dirs = FALSE,
    ignore.case = TRUE,
    pattern = ".*\\.R$"
  )) {
    errors <- lint(file.path(check_path, file),
      linters = linters,
      parse_settings = FALSE
    )
    if (!is.null(errors)) {
      for (error in errors) {
        print(error)
      }
    }
  }
}

if (has_errors) {
  quit(status = 1)
}
quit(status = 0)
