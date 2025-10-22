import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.09961).lineTo(0.0, 0.04551).lineTo(0.0257, 0.06369).lineTo(0.0, 0.09961).close()
solid=wp_sketch0.add(loop0).extrude(-0.05490558585158324)
