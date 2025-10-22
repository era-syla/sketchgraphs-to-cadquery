import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.15841, 0.08462).lineTo(-0.05104, 0.08462).lineTo(-0.05104, 0.03263).lineTo(-0.15841, 0.03263).lineTo(-0.15841, 0.08462).close()
solid=wp_sketch0.add(loop0).extrude(0.03763993592782944)
