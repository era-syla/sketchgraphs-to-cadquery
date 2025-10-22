import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00101, 0.00115).lineTo(0.07875, 0.0472).lineTo(0.07862, 0.04366).lineTo(0.00154, -0.00085).lineTo(-0.00101, 0.00115).close()
solid=wp_sketch0.add(loop0).extrude(0.10688150511842903)
