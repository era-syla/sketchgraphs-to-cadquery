import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02312, -0.02087).lineTo(-0.02312, -0.02087).lineTo(-0.02312, -0.03654).lineTo(0.02312, -0.03654).lineTo(0.02312, -0.02087).close()
solid=wp_sketch0.add(loop0).extrude(0.13412777190516154)
