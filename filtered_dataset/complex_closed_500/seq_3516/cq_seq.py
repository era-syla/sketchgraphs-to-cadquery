import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.08239, 0.01739).lineTo(0.08239, 0.02259).lineTo(0.135, 0.02259).lineTo(0.135, 0.01739).lineTo(0.08239, 0.01739).close()
solid=wp_sketch0.add(loop0).extrude(0.0718702370587537)
