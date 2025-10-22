import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(23.93398, 1.5996).lineTo(21.35527, 1.5996).lineTo(21.35527, 5.05025).lineTo(23.93398, 5.05025).lineTo(23.93398, 1.5996).close()
solid=wp_sketch0.add(loop0).extrude(1.9107778019371169)
