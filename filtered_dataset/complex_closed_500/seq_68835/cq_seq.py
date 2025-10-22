import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.12796, -0.01171).lineTo(-0.12796, -0.01171).lineTo(-0.12796, 0.01171).lineTo(0.12796, 0.01171).lineTo(0.12796, -0.01171).close()
solid=wp_sketch0.add(loop0).extrude(-0.6489838494219571)
