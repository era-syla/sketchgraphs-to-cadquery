import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01475, 0.08397).lineTo(-0.14525, 0.08397).lineTo(-0.14525, 0.04397).lineTo(0.01475, 0.04397).lineTo(0.01475, 0.08397).close()
solid=wp_sketch0.add(loop0).extrude(0.3783945896004902)
