#!/usr/bin/env ruby1.9.1
# encoding: UTF-8

# Requires Ruby 1.9.1 for its order-retaining hashes.

require 'yaml'

data = YAML.load_file(ARGV[0])

open('output.yaml', 'w') do |f|
  YAML::dump(data, f)
end
