import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.2187, 0.0265).lineTo(0.2194, 0.0265).lineTo(0.2194, 0.0135).lineTo(-0.2187, 0.0135).lineTo(-0.2187, 0.0265).close()
solid=wp_sketch0.add(loop0).extrude(0.2787776725689121)
