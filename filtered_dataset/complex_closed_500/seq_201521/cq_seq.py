import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00798, 0.00635).lineTo(-0.00163, 0.00635).lineTo(-0.00163, -0.00635).lineTo(-0.00798, -0.00635).lineTo(-0.00798, 0.00635).close()
solid=wp_sketch0.add(loop0).extrude(0.016182877088970864)
