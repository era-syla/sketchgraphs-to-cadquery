import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.071, 0.00451).lineTo(-0.071, 0.02137).lineTo(-0.056, 0.02137).lineTo(-0.056, 0.00451).lineTo(-0.071, 0.00451).close()
solid=wp_sketch0.add(loop0).extrude(0.02131490562226663)
