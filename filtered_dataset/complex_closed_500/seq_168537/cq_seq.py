import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.15558, -0.03347).lineTo(-0.15558, -0.03347).lineTo(-0.15558, -0.03665).lineTo(0.15558, -0.03665).lineTo(0.15558, -0.03347).close()
solid=wp_sketch0.add(loop0).extrude(0.8413958084395738)
