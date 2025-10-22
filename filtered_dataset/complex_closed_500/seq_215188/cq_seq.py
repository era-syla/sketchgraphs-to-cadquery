import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0025, -0.01).lineTo(0.0, -0.01).lineTo(0.0, 0.0).lineTo(-0.0025, 0.0).lineTo(-0.0025, -0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.0028437374432011974)
