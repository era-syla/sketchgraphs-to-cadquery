import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0127, -0.02959).lineTo(-0.0127, -0.02959).lineTo(-0.01603, -0.01321).lineTo(0.01603, -0.01321).lineTo(0.0127, -0.02959).close()
solid=wp_sketch0.add(loop0).extrude(-0.08925278175853738)
