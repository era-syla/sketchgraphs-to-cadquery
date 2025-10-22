import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0672, 0.07).lineTo(-0.0128, 0.07).lineTo(-0.0128, -0.07).lineTo(0.0672, -0.07).lineTo(0.0672, 0.07).close()
solid=wp_sketch0.add(loop0).extrude(0.13475120066642574)
