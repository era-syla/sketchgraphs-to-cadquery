import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0057, -0.00178).lineTo(0.01095, -0.0086).lineTo(0.01095, -0.01275).lineTo(-0.0057, -0.01275).lineTo(-0.0057, -0.00178).close()
solid=wp_sketch0.add(loop0).extrude(-0.04595042135049715)
