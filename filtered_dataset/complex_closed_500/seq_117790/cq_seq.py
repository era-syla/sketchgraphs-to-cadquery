import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05233, 0.04991).lineTo(0.05112, 0.04991).lineTo(0.05112, -0.0448).lineTo(-0.05233, -0.0448).lineTo(-0.05233, 0.04991).close()
solid=wp_sketch0.add(loop0).extrude(0.08160203362849289)
