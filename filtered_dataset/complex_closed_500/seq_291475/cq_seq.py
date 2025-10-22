import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.12271, 0.461).lineTo(-0.11299, 0.461).lineTo(-0.11299, 0.46232).lineTo(-0.12271, 0.46232).lineTo(-0.12271, 0.461).close()
solid=wp_sketch0.add(loop0).extrude(-0.004869159629684872)
