import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01125, 0.0).lineTo(0.01925, 0.0).lineTo(0.01925, 0.005).lineTo(0.01125, 0.005).lineTo(0.01125, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.005005265866911032)
