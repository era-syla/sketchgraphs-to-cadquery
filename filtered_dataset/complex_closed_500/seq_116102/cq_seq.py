import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.07, 0.0).lineTo(0.035, 0.0).lineTo(0.035, 0.7).lineTo(0.07, 0.7).lineTo(0.07, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-1.1836922213300052)
