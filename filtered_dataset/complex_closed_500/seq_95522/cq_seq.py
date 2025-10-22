import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.005, 0.10955).lineTo(0.005, 0.02063).lineTo(0.04311, 0.005).lineTo(0.04311, -0.009).lineTo(0.07201, -0.009).lineTo(0.07201, 0.005).lineTo(0.10955, 0.02063).lineTo(0.10955, 0.10955).lineTo(0.005, 0.10955).close()
solid=wp_sketch0.add(loop0).extrude(-0.2613029180839416)
