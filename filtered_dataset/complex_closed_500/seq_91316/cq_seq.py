import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00795, 0.13807).lineTo(-0.00371, 0.13807).lineTo(-0.00371, 0.11686).lineTo(-0.00795, 0.11686).lineTo(-0.00795, 0.13807).close()
solid=wp_sketch0.add(loop0).extrude(0.055277238970481146)
