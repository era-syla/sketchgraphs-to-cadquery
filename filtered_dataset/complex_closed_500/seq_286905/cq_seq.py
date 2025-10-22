import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.04234, -0.00241).lineTo(0.04234, 0.00465).lineTo(0.03528, 0.00465).lineTo(0.04234, -0.00241).close()
solid=wp_sketch0.add(loop0).extrude(-0.0009760321604292148)
