import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.09641, -0.05402).lineTo(-0.07216, -0.05402).lineTo(-0.07216, -0.03628).lineTo(-0.09641, -0.03628).lineTo(-0.09641, -0.05402).close()
solid=wp_sketch0.add(loop0).extrude(-0.05560310456035759)
