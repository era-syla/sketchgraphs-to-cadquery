import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0413, -0.03015).lineTo(-0.02516, -0.03015).lineTo(-0.02516, -0.03315).lineTo(-0.0413, -0.03315).lineTo(-0.0413, -0.03015).close()
solid=wp_sketch0.add(loop0).extrude(0.046881433100872366)
