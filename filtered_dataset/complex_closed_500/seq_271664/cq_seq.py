import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.04, 0.0042).lineTo(0.033, 0.0042).lineTo(0.033, -0.0042).lineTo(0.04, -0.0042).lineTo(0.04, 0.0042).close()
solid=wp_sketch0.add(loop0).extrude(0.02251814524440875)
