import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0427, -0.03292).lineTo(-0.0427, 0.04328).lineTo(0.0589, 0.04328).lineTo(0.0589, 0.03375).lineTo(-0.03317, 0.03375).lineTo(-0.03317, -0.03292).lineTo(-0.0427, -0.03292).close()
solid=wp_sketch0.add(loop0).extrude(0.03960017557277633)
