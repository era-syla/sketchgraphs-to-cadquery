import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01, -0.01).lineTo(-0.01, -0.01).lineTo(-0.01, 0.01).lineTo(0.01, 0.01).lineTo(0.01, -0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.04165788119429076)
