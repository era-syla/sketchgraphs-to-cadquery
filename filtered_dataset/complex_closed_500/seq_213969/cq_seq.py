import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02756, -0.006).threePointArc((0.02727, -0.01773), (0.039, -0.01744)).lineTo(0.039, -0.02644).lineTo(0.045, -0.02644).lineTo(0.045, 0.0).lineTo(0.01856, 0.0).lineTo(0.01856, -0.006).lineTo(0.02756, -0.006).close()
solid=wp_sketch0.add(loop0).extrude(0.029806282536140708)
