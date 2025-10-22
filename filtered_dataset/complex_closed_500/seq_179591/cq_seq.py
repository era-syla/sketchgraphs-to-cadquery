import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01, -0.003).lineTo(0.01, -0.003).lineTo(0.01, 0.01111).lineTo(-0.17468, 0.01111).lineTo(-0.17468, -0.02104).lineTo(-0.01, -0.02104).lineTo(-0.01, -0.003).close()
solid=wp_sketch0.add(loop0).extrude(0.3732664373427417)
