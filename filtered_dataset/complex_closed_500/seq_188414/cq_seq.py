import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04647, -0.0097).lineTo(0.04739, -0.01025).lineTo(0.04739, 0.01289).lineTo(-0.04647, 0.01289).lineTo(-0.04647, -0.0097).close()
solid=wp_sketch0.add(loop0).extrude(0.151425795796038)
