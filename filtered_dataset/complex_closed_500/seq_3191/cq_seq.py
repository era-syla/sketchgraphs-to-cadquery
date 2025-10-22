import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.107, 0.0244).lineTo(0.12, 0.0244).lineTo(0.12, 0.0124).lineTo(0.107, 0.0124).lineTo(0.107, 0.0244).close()
solid=wp_sketch0.add(loop0).extrude(0.023951605165022257)
