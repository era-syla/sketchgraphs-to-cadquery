import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00736, -0.03091).lineTo(-0.05286, -0.03091).lineTo(-0.05286, 0.12009).lineTo(0.03814, 0.12009).lineTo(0.03814, -0.03091).lineTo(-0.00736, -0.03091).close()
solid=wp_sketch0.add(loop0).extrude(-0.42034506464952404)
