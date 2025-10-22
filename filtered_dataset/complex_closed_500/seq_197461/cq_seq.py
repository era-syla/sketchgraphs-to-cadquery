import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02103, 0.0254).lineTo(0.02738, 0.0254).lineTo(0.02738, 0.01498).lineTo(0.02103, 0.01498).lineTo(0.02103, 0.0254).close()
solid=wp_sketch0.add(loop0).extrude(-0.00031485419849032974)
