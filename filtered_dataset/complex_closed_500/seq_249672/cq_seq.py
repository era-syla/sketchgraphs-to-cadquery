import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00795, 0.00383).lineTo(0.00654, 0.00648).lineTo(0.01325, 0.01005).lineTo(0.01466, 0.0074).lineTo(0.00795, 0.00383).close()
solid=wp_sketch0.add(loop0).extrude(-0.02261848594769671)
