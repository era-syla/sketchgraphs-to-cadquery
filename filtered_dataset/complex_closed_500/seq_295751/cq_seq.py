import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02261, 0.015).lineTo(-0.0, -0.02415).lineTo(0.02261, 0.015).lineTo(0.0, -0.0).lineTo(-0.02261, 0.015).close()
solid=wp_sketch0.add(loop0).extrude(0.028317477682765577)
