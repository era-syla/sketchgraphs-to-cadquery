import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0123, -0.01161).lineTo(-0.12713, -0.01161).lineTo(-0.12713, 0.08836).lineTo(0.0123, 0.08836).lineTo(0.0123, -0.01161).close()
solid=wp_sketch0.add(loop0).extrude(0.2135428634038616)
