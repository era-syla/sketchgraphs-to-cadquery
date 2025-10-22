import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0101, -0.02926).lineTo(0.0118, -0.03076).lineTo(0.002, -0.03076).lineTo(0.002, -0.02926).lineTo(0.0101, -0.02926).close()
solid=wp_sketch0.add(loop0).extrude(0.00502806659436113)
