import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01, 0.025).lineTo(0.01, 0.025).lineTo(0.01, 0.005).lineTo(-0.01, 0.005).lineTo(-0.01, 0.025).close()
solid=wp_sketch0.add(loop0).extrude(-0.021810233031905196)
