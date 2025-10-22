import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0229, 0.02291).lineTo(-0.01966, 0.02291).lineTo(-0.01966, 0.00617).lineTo(-0.0312, 0.00617).lineTo(-0.0312, 0.02288).lineTo(-0.0229, 0.02291).close()
solid=wp_sketch0.add(loop0).extrude(-0.0009975333817956935)
