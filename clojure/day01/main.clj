(ns mulli.aoc
  (:require [clojure.string :as str]))

(def INPUT-FILENAME "../../inputs/day01.input")
(print "Starting...")

(defn print-each [items]
  (doseq [i items]
    (println i)))

; read
(def input (slurp INPUT-FILENAME))
;(println input)

; split by line
(defn split-on-newline [raw]
  (str/split raw #"\n"))

; map across each line
(print-each (filterv #(Character/isDigit %) (seq (seq (split-on-newline input)))))

;(println (filterv #(Character/isDigit %) (seq "xyz12abc")))

; take only non-digits



; cat the FIRST and LAST digits to make number (could be 1,2, or more digits)



; sum all numbers



; report/print
