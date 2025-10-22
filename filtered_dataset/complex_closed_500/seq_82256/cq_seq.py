import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.036, 0.04).lineTo(0.036, 0.04).lineTo(0.036, -0.04).lineTo(-0.036, -0.04).lineTo(-0.036, 0.04).close()
solid=wp_sketch0.add(loop0).extrude(-0.09523100209906954)
