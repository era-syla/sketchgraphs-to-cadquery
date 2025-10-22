import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05819, -0.00798).lineTo(-0.03553, -0.00798).lineTo(-0.03553, 0.0085).lineTo(-0.05819, 0.0085).lineTo(-0.05819, -0.00798).close()
solid=wp_sketch0.add(loop0).extrude(-0.06729209503717418)
