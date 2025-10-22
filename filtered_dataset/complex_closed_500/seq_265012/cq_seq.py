import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00247, 0.0091).lineTo(0.01453, 0.0091).lineTo(0.01453, 0.00867).lineTo(-0.00247, 0.00867).lineTo(-0.00247, 0.0091).close()
solid=wp_sketch0.add(loop0).extrude(-0.03767388795835405)
