import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02736, 0.12271).lineTo(0.05327, 0.12271).lineTo(0.05327, 0.05255).lineTo(0.02736, 0.05255).lineTo(0.02736, 0.12271).close()
solid=wp_sketch0.add(loop0).extrude(-0.10871642741846764)
