import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, -0.01).lineTo(-0.005, -0.01).lineTo(-0.005, -0.0).lineTo(-0.025, 0.0).lineTo(-0.025, 0.045).lineTo(-0.02, 0.045).lineTo(-0.02, 0.01).lineTo(0.0, 0.00647).lineTo(-0.0, -0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.06303093293881969)
