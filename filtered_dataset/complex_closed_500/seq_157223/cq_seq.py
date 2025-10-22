import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0253, 0.0048).lineTo(0.0253, 0.0048).lineTo(0.0253, 0.0028).lineTo(-0.0253, 0.0028).lineTo(-0.0253, 0.0048).close()
solid=wp_sketch0.add(loop0).extrude(0.11858441899358284)
