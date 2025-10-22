import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0218, 0.01187).lineTo(-0.01022, 0.01187).lineTo(-0.01022, 0.0).lineTo(-0.0218, 0.0).lineTo(-0.0218, 0.01187).close()
solid=wp_sketch0.add(loop0).extrude(-0.0021971851204610256)
