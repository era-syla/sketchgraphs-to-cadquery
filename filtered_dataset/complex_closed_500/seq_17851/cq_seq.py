import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.09049, -0.0).lineTo(-0.15459, -0.0).lineTo(-0.15459, -0.0436).lineTo(-0.09049, -0.0436).lineTo(-0.09049, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.025615947055345766)
