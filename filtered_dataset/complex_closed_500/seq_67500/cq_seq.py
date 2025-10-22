import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.41642, 0.2046).lineTo(0.33576, 0.2046).lineTo(0.33576, 0.15412).lineTo(0.41642, 0.15412).lineTo(0.41642, 0.2046).close()
solid=wp_sketch0.add(loop0).extrude(-0.08233043130554825)
